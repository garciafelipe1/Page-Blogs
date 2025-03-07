from celery import shared_task


import logging 

from .models import PostAnalytics

logger = logging.getLogger(__name__)

@shared_task
def increment_post_impressions(post_id):
    """
    Task to increment post impressions
    """
    
    try:
        analytics,created=PostAnalytics.objects.get_or_create(post__id=post_id)
        analytics.increment_impressions()
    except Exception as e:
        logger.info(f"An error ocurred while updating post analytics: {str(e)}")

