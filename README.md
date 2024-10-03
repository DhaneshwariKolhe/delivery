# Real-Time Tracking System

This Django project implements a real-time tracking system using Kafka, OpenStreetMap (OSM), and Leaflet.js.

## Project Overview

This application provides real-time tracking capabilities, visualized on an interactive map. It leverages the power of Django for the backend, Kafka for real-time data streaming, and OpenStreetMap with Leaflet.js for map rendering and interaction.

## Technologies Used

- **Backend Framework**: Django
- **Real-Time Messaging**: Apache Kafka
- **Map Data**: OpenStreetMap (OSM)
- **Map Rendering**: Leaflet.js

## Features

- Real-time tracking of objects/vehicles
- Interactive map interface using OpenStreetMap
- Seamless updates through Kafka messaging system

## Setup and Installation

1. Clone the repository
2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up Kafka and configure connection settings
4. Run Django migrations:
   ```
   python manage.py migrate
   ```
5. Start the Django development server:
   ```
   python manage.py runserver
   ```

## Usage

[Provide instructions on how to use the application, including any necessary API endpoints or user interface guidelines]

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

