from setuptools import setup, find_packages

setup(
    name='flask_postgres_app',
    version='1.0.0',
    description='Flask app with PostgreSQL',
    author='Valeria Zaborovskaia',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'psycopg2-binary'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-flask',
            'pytest-cov'
        ],
    },
    entry_points={
        'console_scripts': [
            'flask_postgres_app=app.app:main',
        ],
    },
)
