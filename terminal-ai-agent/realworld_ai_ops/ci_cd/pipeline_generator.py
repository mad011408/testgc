"""
Pipeline Generator - Generates CI/CD pipeline definitions.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class PipelineType(str, Enum):
    GITHUB_ACTIONS = "github_actions"
    GITLAB_CI = "gitlab_ci"
    JENKINS = "jenkins"
    AZURE_DEVOPS = "azure_devops"


@dataclass
class PipelineStage:
    name: str
    jobs: List[Dict[str, Any]]
    depends_on: List[str] = field(default_factory=list)


@dataclass
class PipelineDefinition:
    name: str
    type: PipelineType
    stages: List[PipelineStage]
    triggers: List[str] = field(default_factory=lambda: ["push", "pull_request"])
    variables: Dict[str, str] = field(default_factory=dict)


class PipelineGenerator:
    """Generates CI/CD pipeline configs from templates."""

    def __init__(self, default_type: PipelineType = PipelineType.GITHUB_ACTIONS):
        self.default_type = default_type

    def generate_python_pipeline(
        self,
        python_version: str = "3.11",
        test_command: str = "pytest",
        build_steps: Optional[List[Dict]] = None,
    ) -> PipelineDefinition:
        """Generate Python project pipeline."""
        stages = [
            PipelineStage(
                name="test",
                jobs=[
                    {"name": "lint", "run": "ruff check ."},
                    {"name": "test", "run": test_command},
                ],
            ),
            PipelineStage(
                name="build",
                jobs=build_steps or [{"name": "build", "run": "pip wheel . -w dist/"}],
                depends_on=["test"],
            ),
        ]
        return PipelineDefinition(
            name="python-pipeline",
            type=self.default_type,
            stages=stages,
            variables={"PYTHON_VERSION": python_version},
        )

    def generate_docker_pipeline(
        self,
        image_name: str,
        registry: str = "ghcr.io",
    ) -> PipelineDefinition:
        """Generate Docker build pipeline."""
        stages = [
            PipelineStage(
                name="build",
                jobs=[
                    {"name": "docker-build", "image": "docker:24", "args": [image_name]},
                ],
            ),
            PipelineStage(
                name="push",
                jobs=[{"name": "docker-push", "registry": registry, "image": image_name}],
                depends_on=["build"],
            ),
        ]
        return PipelineDefinition(name="docker-pipeline", type=self.default_type, stages=stages)

    def to_yaml(self, pipeline: PipelineDefinition) -> str:
        """Export pipeline to YAML (stub)."""
        lines = [f"# {pipeline.name}", f"type: {pipeline.type.value}"]
        for stage in pipeline.stages:
            lines.append(f"- stage: {stage.name}")
            for job in stage.jobs:
                lines.append(f"  job: {job.get('name', 'unnamed')}")
        return "\n".join(lines)
