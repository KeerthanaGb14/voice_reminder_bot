# Voice Reminder Bot (ROS2)

## Overview
The **Voice Reminder Bot** is a ROS2-based application that allows users to set voice-activated reminders. The system listens for spoken commands, parses the reminder text, schedules notifications, and notifies the user at the appropriate time.

This project is built with Python and ROS2 (Humble), following a modular node-based architecture.

---

## Features
- **Speech Listener Node:** Continuously listens for voice commands and publishes reminders.
- **Reminder Parser Node:** Processes incoming reminders and extracts relevant information.
- **Scheduler Node:** Schedules reminders based on the parsed data.
- **Notifier Node:** Sends notifications for scheduled reminders.

---

## Architecture

