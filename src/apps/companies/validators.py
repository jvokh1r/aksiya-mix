from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.general.variables import COMPANY_VIDEO_MAX_SIZE

def validate_company_video_size(video_file):
    if video_file.size > COMPANY_VIDEO_MAX_SIZE:
        raise ValidationError(_('video size must be less than 10 MB!'))
