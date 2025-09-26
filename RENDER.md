# Deploying to Render.com

This document explains how to deploy the Flask application to Render.com.

## Prerequisites

1. A Render.com account
2. This GitHub repository (https://github.com/minhaaj-t/test-server)

## Deployment Steps

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub account if you haven't already
4. Select the repository `minhaaj-t/test-server`
5. Configure the following settings:
   - Name: `test-server` (or any name you prefer)
   - Region: Choose the region closest to you
   - Branch: `main`
   - Root Directory: Leave empty
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
6. Add the following environment variables (using the values from your .env file):
   - `DB_HOST`: db.fr-pari1.bengt.wasmernet.com
   - `DB_PORT`: 10272
   - `DB_NAME`: library_management
   - `DB_USER`: 7e4ca751759c8000463db46b28a7
   - `DB_PASSWORD`: 068b7e4c-a751-77af-8000-cb2911e1c700
7. Click "Create Web Service"

## How it Works

Render will automatically:
1. Clone your repository
2. Install dependencies using `requirements.txt`
3. Use the `Procfile` to know how to start your application
4. Use the `runtime.txt` to determine the Python version
5. Set the `PORT` environment variable automatically

The application is configured to:
- Use the `PORT` environment variable provided by Render
- Connect to your MySQL database using the environment variables
- Create tables and insert dummy data on first run
- Serve both the frontend interface and API endpoints from the same application
- Serve the frontend at the root path (`/`)
- Serve API endpoints under `/api` (e.g., `/api/books`, `/api/products`)

## Environment Variables

Render will automatically set the `PORT` environment variable. Your application should use this for listening.

You need to manually set the following environment variables in the Render dashboard:
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

## Automatic Deployments

Render will automatically rebuild and deploy your application whenever you push changes to the `main` branch of your GitHub repository.

## Manual Deployment

To manually trigger a deployment:
1. Go to your service in the Render dashboard
2. Click "Manual Deploy"
3. Select "Deploy latest commit" or "Clear build cache & deploy"

## Troubleshooting

If your deployment fails:
1. Check the logs in the Render dashboard
2. Ensure all environment variables are correctly set
3. Verify that your database connection details are correct
4. Make sure your requirements.txt includes all necessary packages

If you're getting a "Not Found" error:
1. Make sure your Flask app is configured to serve static files correctly
2. Verify that the frontend files are in the correct directory
3. Check that the routing is set up properly to serve both the frontend and API endpoints

## Scaling

Render automatically handles scaling for you. For more advanced scaling options, you can configure:
- Instance count
- Instance size (CPU and memory)
- Auto-scaling rules

In the Render dashboard, go to your service settings to configure these options.