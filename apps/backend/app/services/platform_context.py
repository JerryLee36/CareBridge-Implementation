from app.services.audit import AuditLogService
from app.services.data_quality import DataQualityService
from app.services.notification import NotificationService
from app.services.rbac import RBACService
from app.services.rule_registry import RuleRegistryService
from app.services.system_config import SystemConfigService
from app.services.trend_analysis import TrendAnalysisService


class PlatformContext:
    def __init__(self) -> None:
        self.data_quality = DataQualityService()
        self.rule_registry = RuleRegistryService()
        self.trend = TrendAnalysisService()
        self.notifications = NotificationService()
        self.rbac = RBACService()
        self.audit = AuditLogService()
        self.system_config = SystemConfigService()


platform_context = PlatformContext()
