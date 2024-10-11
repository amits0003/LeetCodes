"""
write API's for a service which takes out of order video frames but forwards them in order for processing.
Consider your services receives frsmes froom another service which could be out if order but your service
forwards them to another service always in sequence (based on timestamp). After a lot of clarifying questions,
created a class with SaveFrame() and GetFrame() functions using unordered_map and list. Discussed in length about
concurrency problems and resolved some issues using mutexes and double locking approach.
"""

import threading
from collections import deque


class FrameService:
    def __init__(self):
        # Dictionary to store frames indexed by timestamp
        self.frames = {}
        # Deque to store frames in order for quick pop from the front
        self.ordered_frames = deque()
        # Mutex for handling concurrent access
        self.lock = threading.RLock()
        # Variable to track the last forwarded timestamp
        self.last_forwarded = None

    def save_frame(self, frame, timestamp):
        """
        Save a frame with its corresponding timestamp.
        Frames may arrive out of order.
        """
        with self.lock:
            # Save the frame in the unordered dictionary
            self.frames[timestamp] = frame
            # Maintain the deque in order of timestamps
            self._insert_frame_in_order(timestamp)

    def _insert_frame_in_order(self, timestamp):
        """
        Inserts a frame in the deque while maintaining the order by timestamp.
        """
        # Use binary search for efficient insertion in the ordered deque
        if not self.ordered_frames or timestamp > self.ordered_frames[-1]:
            self.ordered_frames.append(timestamp)
        else:
            for i, t in enumerate(self.ordered_frames):
                if timestamp < t:
                    self.ordered_frames.insert(i, timestamp)
                    break

    def get_frame(self):
        """
        Retrieve the next frame in sequence based on the timestamp.
        This ensures frames are forwarded in order.
        """
        with self.lock:
            if not self.ordered_frames:
                return None

            next_timestamp = self.ordered_frames[0]
            if self.last_forwarded is None or next_timestamp > self.last_forwarded:
                # Pop the next frame from the deque
                self.last_forwarded = next_timestamp
                self.ordered_frames.popleft()
                # Retrieve the frame from the dictionary
                return self.frames.pop(next_timestamp)
            return None

    def forward_frames(self, process_frame):
        """
        Continuously forward frames to the next service, ensuring they are in order.
        This function can be run in a separate thread.
        """
        while True:
            frame = self.get_frame()
            if frame:
                process_frame(frame)  # Forward to the next service
            else:
                # Sleep for a short time to avoid busy-waiting
                threading.Event().wait(0.1)


# Usage example
def process_frame(frame):
    print(f"Processing frame: {frame}")


# FrameService instance
frame_service = FrameService()

# Simulate adding frames out of order
frame_service.save_frame("Frame 1", 3)
frame_service.save_frame("Frame 2", 1)
frame_service.save_frame("Frame 3", 2)

# Forward frames in the correct order
frame_service.forward_frames(process_frame)
