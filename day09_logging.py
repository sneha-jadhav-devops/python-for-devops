import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("DevOps automation script started")
logging.warning("Low disk space warning")
logging.error("Service failed to start")
