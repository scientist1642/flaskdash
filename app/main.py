"""Application entry point."""

from flask import Flask

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False,
                template_folder='/opt/app/templates',
                static_folder='/opt/app/static'
                )

    with app.app_context():
        # Import parts of our core Flask app
        import routes
        #from .assets import compile_static_assets

        # Import Dash application
        from dashboard import init_dashboard

        app = init_dashboard(app)

        # Compile static assets
        #compile_static_assets(assets)

        return app

app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=int("8080"))