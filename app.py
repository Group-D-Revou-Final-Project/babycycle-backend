# from src.config.settings import create_app
from src.config.settings import create_app
from src.config.settings import db  # Pastikan db diimport untuk membuat tabel
# from src.models.user import User 
# from src.routers.auth import auth_bp



# Main driver function
app = create_app()

# app.register_blueprint(auth_bp, url_prefix='/auth/v1')

if __name__ == '__main__':
    import hypercorn.asyncio
    import asyncio

    with app.app_context():
        db.create_all() 

    asyncio.run(hypercorn.asyncio.serve(app, hypercorn.Config()))
