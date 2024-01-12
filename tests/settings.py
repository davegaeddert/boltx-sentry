from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()

SECRET_KEY = "secret"

DEBUG = True

INSTALLED_PACKAGES = [
    "bolt.auth",
    "bolt.sessions",
    "boltx.sentry",
]

MIDDLEWARE = [
    "bolt.middleware.security.SecurityMiddleware",
    "bolt.sessions.middleware.SessionMiddleware",
    "bolt.middleware.common.CommonMiddleware",
    "bolt.csrf.middleware.CsrfViewMiddleware",
    "bolt.auth.middleware.AuthenticationMiddleware",
    "bolt.middleware.clickjacking.XFrameOptionsMiddleware",
    "boltx.sentry.middleware.SentryFeedbackMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "bolt.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ROOT_URLCONF = "urls"

USE_TZ = True
