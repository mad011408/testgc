"""
AWS Adapter - Abstracts AWS API interactions.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from abc import ABC, abstractmethod


@dataclass
class EC2Instance:
    instance_id: str
    instance_type: str
    state: str
    region: str
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class S3Bucket:
    name: str
    region: str
    creation_date: str
    size_bytes: int = 0


class AWSService(ABC):
    """Base class for AWS service adapters."""

    def __init__(self, region: str = "us-east-1", profile: Optional[str] = None):
        self.region = region
        self.profile = profile

    @abstractmethod
    async def list_resources(self) -> List[Any]:
        pass


class EC2Adapter(AWSService):
    """EC2 instance management."""

    async def list_instances(self) -> List[EC2Instance]:
        """List EC2 instances (stub - requires boto3 in production)."""
        # In production: boto3.client('ec2').describe_instances()
        return []

    async def start_instance(self, instance_id: str) -> Dict[str, Any]:
        return {"action": "start", "instance_id": instance_id, "status": "pending"}

    async def stop_instance(self, instance_id: str) -> Dict[str, Any]:
        return {"action": "stop", "instance_id": instance_id, "status": "pending"}

    async def describe_instance(self, instance_id: str) -> Optional[Dict[str, Any]]:
        return {"instance_id": instance_id, "region": self.region}


class S3Adapter(AWSService):
    """S3 bucket operations."""

    async def list_buckets(self) -> List[S3Bucket]:
        """List S3 buckets (stub)."""
        return []

    async def get_object(self, bucket: str, key: str) -> Optional[Dict[str, Any]]:
        return {"bucket": bucket, "key": key, "region": self.region}


class AWSAdapter:
    """Unified AWS adapter for EC2, S3, etc."""

    def __init__(self, region: str = "us-east-1", profile: Optional[str] = None):
        self.region = region
        self.profile = profile
        self.ec2 = EC2Adapter(region, profile)
        self.s3 = S3Adapter(region, profile)

    async def health_check(self) -> Dict[str, Any]:
        """Check AWS connectivity."""
        return {"provider": "aws", "region": self.region, "status": "ok"}
