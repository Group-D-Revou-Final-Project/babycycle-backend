from src.config.settings import create_app
from src.config.settings import db  # Pastikan db diimport untuk membuat tabel



# Main driver function
app = create_app()

if __name__ == '__main__':
    import hypercorn.asyncio
    import asyncio

    with app.app_context():
        db.create_all() 

    asyncio.run(hypercorn.asyncio.serve(app, hypercorn.Config()))
