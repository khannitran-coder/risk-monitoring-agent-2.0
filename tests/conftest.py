from datetime import date

import pytest

from sprint_risk_agent.audit import AuditLog
from sprint_risk_agent.graph import build_graph
from sprint_risk_agent.mcp_clients.fake import demo_clients

AS_OF = date(2026, 10, 7)


@pytest.fixture
def clients():
    return demo_clients(AS_OF)


@pytest.fixture
def audit():
    return AuditLog()


@pytest.fixture
def graph(clients, audit):
    return build_graph(clients, audit=audit)
