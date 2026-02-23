#!/usr/bin/env python3
"""
Terminal AI Agent - Entry Point
Advanced framework with Rork API, Max Mode (1M token context), multiple models.
Integrated: realworld_ai_ops, coding_superagent, economic_ai, cyber_defense_ai, intelligence, reasoning, planning, shells, protocols, filesystem
"""

import asyncio
import os
import sys
from pathlib import Path

# Ensure project root is on path
_root = Path(__file__).resolve().parent
sys.path.insert(0, str(_root))
os.chdir(_root)

# Integrate all modules
def register_integrated_modules() -> dict:
    """Load and register all integrated AI modules for agent context."""
    modules = {}
    try:
        from realworld_ai_ops.control_plane import orchestrator, infra_state_manager, deployment_controller, rollback_engine
        modules["realworld_ai_ops"] = {
            "control_plane": ["Orchestrator", "InfraStateManager", "DeploymentController", "RollbackEngine"],
        }
    except ImportError:
        pass
    try:
        from realworld_ai_ops.cloud_providers import aws_adapter, gcp_adapter, azure_adapter
        modules["realworld_ai_ops"]["cloud_providers"] = ["AWSAdapter", "GCPAdapter", "AzureAdapter"]
    except (ImportError, KeyError):
        pass
    try:
        from realworld_ai_ops.kubernetes import cluster_manager, pod_controller, autoscaler_ai
        modules["realworld_ai_ops"]["kubernetes"] = ["ClusterManager", "PodController", "AutoscalerAI"]
    except (ImportError, KeyError):
        pass
    try:
        from realworld_ai_ops.ci_cd import pipeline_generator, test_executor, security_scanner
        modules["realworld_ai_ops"]["ci_cd"] = ["PipelineGenerator", "TestExecutor", "SecurityScanner"]
    except (ImportError, KeyError):
        pass
    try:
        from realworld_ai_ops.production_guard import risk_analyzer, blast_radius_estimator, approval_workflow
        modules["realworld_ai_ops"]["production_guard"] = ["RiskAnalyzer", "BlastRadiusEstimator", "ApprovalWorkflow"]
    except (ImportError, KeyError):
        pass
    try:
        from realworld_ai_ops.audit import change_logger, compliance_engine
        modules["realworld_ai_ops"]["audit"] = ["ChangeLogger", "ComplianceEngine"]
    except (ImportError, KeyError):
        pass
    try:
        from coding_superagent.repo_analyzer import code_graph_builder, dependency_mapper, vulnerability_detector
        modules["coding_superagent"] = {
            "repo_analyzer": ["CodeGraphBuilder", "DependencyMapper", "VulnerabilityDetector"],
        }
    except ImportError:
        modules["coding_superagent"] = {}
    try:
        from coding_superagent.auto_refactor import architecture_optimizer, performance_optimizer, tech_debt_reducer
        modules["coding_superagent"]["auto_refactor"] = ["ArchitectureOptimizer", "PerformanceOptimizer", "TechDebtReducer"]
    except (ImportError, KeyError):
        pass
    try:
        from coding_superagent.test_intelligence import auto_test_generator, regression_predictor
        modules["coding_superagent"]["test_intelligence"] = ["AutoTestGenerator", "RegressionPredictor"]
    except (ImportError, KeyError):
        pass
    try:
        from coding_superagent.runtime_feedback import crash_analyzer, log_intelligence
        modules["coding_superagent"]["runtime_feedback"] = ["CrashAnalyzer", "LogIntelligence"]
    except (ImportError, KeyError):
        pass
    try:
        from coding_superagent.patch_deployer import hotfix_engine, safe_merge_controller
        modules["coding_superagent"]["patch_deployer"] = ["HotfixEngine", "SafeMergeController"]
    except (ImportError, KeyError):
        pass
    try:
        from economic_ai.market_analysis import data_ingestion, anomaly_detector, signal_generator
        modules["economic_ai"] = {"market_analysis": ["DataIngestion", "AnomalyDetector", "SignalGenerator"]}
    except ImportError:
        modules["economic_ai"] = {}
    try:
        from economic_ai.risk_management import exposure_calculator, volatility_estimator, portfolio_balancer
        modules["economic_ai"]["risk_management"] = ["ExposureCalculator", "VolatilityEstimator", "PortfolioBalancer"]
    except (ImportError, KeyError):
        pass
    try:
        from economic_ai.decision_core import strategy_selector, execution_engine
        modules["economic_ai"]["decision_core"] = ["StrategySelector", "ExecutionEngine"]
    except (ImportError, KeyError):
        pass
    try:
        from economic_ai.compliance import regulatory_checker
        modules["economic_ai"]["compliance"] = ["RegulatoryChecker"]
    except (ImportError, KeyError):
        pass
    try:
        from cyber_defense_ai.network_monitoring import traffic_analyzer, intrusion_detector
        modules["cyber_defense_ai"] = {"network_monitoring": ["TrafficAnalyzer", "IntrusionDetector"]}
    except ImportError:
        modules["cyber_defense_ai"] = {}
    try:
        from cyber_defense_ai.anomaly_detection import behavior_model, threat_classifier
        modules["cyber_defense_ai"]["anomaly_detection"] = ["BehaviorModel", "ThreatClassifier"]
    except (ImportError, KeyError):
        pass
    try:
        from cyber_defense_ai.response_engine import auto_isolation, firewall_updater
        modules["cyber_defense_ai"]["response_engine"] = ["AutoIsolation", "FirewallUpdater"]
    except (ImportError, KeyError):
        pass
    try:
        from cyber_defense_ai.forensic_module import attack_reconstructor
        modules["cyber_defense_ai"]["forensic_module"] = ["AttackReconstructor"]
    except (ImportError, KeyError):
        pass
    # Intelligence - AI Intelligence Core
    try:
        from intelligence import (
            iq_engine, problem_solver, pattern_recognizer, anomaly_detector,
            prediction_engine, decision_tree, monte_carlo, bayesian_engine, fuzzy_logic,
            genetic_algorithm, neural_network, reinforcement, evolutionary, swarm_intelligence,
        )
        modules["intelligence"] = {
            "core": [
                "IqEngine", "ProblemSolver", "PatternRecognizer", "AnomalyDetector", "PredictionEngine",
                "DecisionTree", "MonteCarlo", "BayesianEngine", "FuzzyLogic", "GeneticAlgorithm",
                "NeuralNetwork", "ReinforcementEngine", "EvolutionaryEngine", "SwarmIntelligence",
            ],
        }
    except ImportError:
        pass
    # Reasoning - Advanced Reasoning
    try:
        from reasoning import (
            chain_of_thought, tree_of_thought, graph_of_thought, reflexion, self_consistency,
            least_to_most, decomposition, analogical, causal, abductive, inductive, deductive,
            counterfactual, meta_reasoning, multi_step,
        )
        modules["reasoning"] = {
            "core": [
                "ChainOfThought", "TreeOfThought", "GraphOfThought", "Reflexion", "SelfConsistency",
                "LeastToMost", "Decomposition", "AnalogicalReasoning", "CausalReasoning", "AbductiveReasoning",
                "InductiveReasoning", "DeductiveReasoning", "CounterfactualReasoning", "MetaReasoning", "MultiStepReasoning",
            ],
        }
    except ImportError:
        pass
    # Planning - Strategic Planning
    try:
        from planning import (
            strategic_planner, tactical_planner, operational_planner, hierarchical_planner,
            graph_planner, constraint_planner, probabilistic_planner, contingency_planner,
            resource_planner, schedule_planner, path_planner, goal_oriented, behavior_tree, finite_state,
        )
        modules["planning"] = {
            "core": [
                "StrategicPlanner", "TacticalPlanner", "OperationalPlanner", "HierarchicalPlanner",
                "GraphPlanner", "ConstraintPlanner", "ProbabilisticPlanner", "ContingencyPlanner",
                "ResourcePlanner", "SchedulePlanner", "PathPlanner", "GoalOrientedPlanner", "BehaviorTree", "FiniteStatePlanner",
            ],
        }
    except ImportError:
        pass
    # Shells - Shell Management
    try:
        from shells import (
            shell_manager, shell_detector, shell_launcher, shell_controller, shell_communicator,
            shell_configurator, shell_profile_loader, shell_rc_parser, shell_environment,
            shell_integration, shell_prompt_parser,
        )
        from shells.implementations import (
            base_shell, bash_shell, zsh_shell, fish_shell, dash_shell, ash_shell, sh_shell,
            ksh_shell, tcsh_shell, csh_shell, powershell_shell, pwsh_shell, cmd_shell,
            nushell_shell, xonsh_shell, elvish_shell, oil_shell,
        )
        from shells.builtins import (
            cd_handler, pwd_handler, export_handler, alias_handler, history_handler,
            source_handler, exit_handler, jobs_handler, fg_bg_handler, pushd_popd_handler,
            set_handler, unset_handler, builtin_registry,
        )
        modules["shells"] = {
            "core": [
                "ShellManager", "ShellDetector", "ShellLauncher", "ShellController", "ShellCommunicator",
                "ShellConfigurator", "ShellProfileLoader", "ShellRCParser", "ShellEnvironment",
                "ShellIntegration", "ShellPromptParser",
            ],
            "implementations": [
                "BaseShell", "BashShell", "ZshShell", "FishShell", "DashShell", "AshShell", "ShShell",
                "KshShell", "TcshShell", "CshShell", "PowerShellShell", "PwshShell", "CmdShell",
                "NushellShell", "XonshShell", "ElvishShell", "OilShell",
            ],
            "builtins": [
                "CdHandler", "PwdHandler", "ExportHandler", "AliasHandler", "HistoryHandler",
                "SourceHandler", "ExitHandler", "JobsHandler", "FgBgHandler", "PushdPopdHandler",
                "SetHandler", "UnsetHandler", "BuiltinRegistry",
            ],
        }
    except ImportError:
        pass
    # Protocols - Terminal Protocols
    try:
        from protocols import (
            protocol_manager, local_protocol, ssh_protocol, mosh_protocol, telnet_protocol,
            rlogin_protocol, serial_protocol, websocket_protocol, tcp_protocol,
            unix_socket_protocol, container_protocol,
        )
        modules["protocols"] = {
            "core": [
                "ProtocolManager", "LocalProtocol", "SshProtocol", "MoshProtocol", "TelnetProtocol",
                "RloginProtocol", "SerialProtocol", "WebSocketProtocol", "TcpProtocol",
                "UnixSocketProtocol", "ContainerProtocol",
            ],
        }
    except ImportError:
        pass
    # Filesystem - FS Engine
    try:
        from filesystem import fs_engine, fs_controller
        from filesystem.operations import (
            file_ops, file_create, file_read, file_write, file_append, file_delete,
            file_rename, file_copy, file_move, file_link, file_truncate, file_touch,
            file_lock, file_unlock, atomic_write, safe_save, temp_file, backup_on_write,
        )
        from filesystem.directory import (
            dir_ops, dir_create, dir_delete, dir_rename, dir_copy, dir_move,
            dir_list, dir_walk, dir_size, dir_sync, dir_compare, dir_merge, temp_dir,
        )
        from filesystem.path import (
            path_manager, path_resolver, path_normalizer, path_validator, path_builder,
            path_matcher, glob_handler, fnmatch_handler, realpath_handler,
            symlink_resolver, relative_path,
        )
        from filesystem.permissions import (
            permission_manager, mode_handler, owner_handler, group_handler,
            acl_handler, capability_handler, xattr_handler, selinux_context,
            apparmor_context, umask_handler,
        )
        from filesystem.watching import (
            watcher_manager, inotify_watcher, fsevents_watcher, kqueue_watcher,
            win_watcher, polling_watcher, recursive_watcher, filter_watcher,
            debounced_watcher, event_coalescer,
        )
        from filesystem.search import (
            search_engine, filename_search, content_search, regex_search, fuzzy_search,
            semantic_search, indexed_search, mlocate_search, fd_search, rg_search, ag_search,
        )
        from filesystem.analysis import (
            file_analyzer, file_type, mime_detector, magic_handler, encoding_detector,
            line_ending, binary_detector, size_analyzer, metadata_extractor,
            checksum_calculator, diff_analyzer, duplicate_finder,
        )
        modules["filesystem"] = {
            "core": ["FSEngine", "FSController"],
            "operations": [
                "FileOps", "FileCreate", "FileRead", "FileWrite", "FileAppend", "FileDelete",
                "FileRename", "FileCopy", "FileMove", "FileLink", "FileTruncate", "FileTouch",
                "FileLock", "FileUnlock", "AtomicWrite", "SafeSave", "TempFile", "BackupOnWrite",
            ],
            "directory": [
                "DirOps", "DirCreate", "DirDelete", "DirRename", "DirCopy", "DirMove",
                "DirList", "DirWalk", "DirSize", "DirSync", "DirCompare", "DirMerge", "TempDir",
            ],
            "path": [
                "PathManager", "PathResolver", "PathNormalizer", "PathValidator", "PathBuilder",
                "PathMatcher", "GlobHandler", "FnmatchHandler", "RealpathHandler",
                "SymlinkResolver", "RelativePath",
            ],
            "permissions": [
                "PermissionManager", "ModeHandler", "OwnerHandler", "GroupHandler",
                "AclHandler", "CapabilityHandler", "XattrHandler", "SelinuxContext",
                "ApparmorContext", "UmaskHandler",
            ],
            "watching": [
                "WatcherManager", "InotifyWatcher", "FseventsWatcher", "KqueueWatcher",
                "WinWatcher", "PollingWatcher", "RecursiveWatcher", "FilterWatcher",
                "DebouncedWatcher", "EventCoalescer",
            ],
            "search": [
                "SearchEngine", "FilenameSearch", "ContentSearch", "RegexSearch", "FuzzySearch",
                "SemanticSearch", "IndexedSearch", "MlocateSearch", "FdSearch", "RgSearch", "AgSearch",
            ],
            "analysis": [
                "FileAnalyzer", "FileType", "MimeDetector", "MagicHandler", "EncodingDetector",
                "LineEnding", "BinaryDetector", "SizeAnalyzer", "MetadataExtractor",
                "ChecksumCalculator", "DiffAnalyzer", "DuplicateFinder",
            ],
        }
    except ImportError:
        pass
    return modules


if __name__ == "__main__":
    # Pre-load and integrate all modules for agent
    _modules = register_integrated_modules()
    from src.agent import main
    asyncio.run(main(integrated_modules=_modules))
