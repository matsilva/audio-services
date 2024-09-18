# logging_config.py
import os
import structlog

# Check if we're in development mode
if os.getenv("ENV") == "production":
    renderer = structlog.processors.JSONRenderer()
else:
    renderer = structlog.dev.ConsoleRenderer()

# Structlog configuration
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        renderer,  # Either ConsoleRenderer for development or JSONRenderer for production
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Create a logger instance
logger = structlog.get_logger()
