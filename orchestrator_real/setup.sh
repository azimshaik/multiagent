#!/bin/bash

# Set up environment variables for ADK and Google Cloud
export GOOGLE_CLOUD_PROJECT=$(gcloud config get project)
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_LOCATION="us-central1"

echo "Environment configured for Project: $GOOGLE_CLOUD_PROJECT"
echo "Installing dependencies..."
pip install -r requirements.txt
