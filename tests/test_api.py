import pytest
import networkx as nx


from obsidiantools.api import Vault


@pytest.fixture
def mock_initial_vault(tmp_path):
    mock_vault = Vault(tmp_path)
    return mock_vault


def test_vault_instantiation(tmp_path):
    actual_vault = Vault(tmp_path)

    assert isinstance(actual_vault, Vault)

    # dirpath
    assert actual_vault.dirpath == tmp_path

    # file_index
    assert isinstance(actual_vault.file_index, dict)

    # graph and connections
    assert not actual_vault.graph
    assert actual_vault.graph is None
    assert not actual_vault.is_connected
    assert isinstance(actual_vault.is_connected, bool)
    assert actual_vault.backlinks_index == {}
    assert actual_vault.wikilinks_index == {}
    assert actual_vault.embedded_files_index == {}
    assert actual_vault.math_index == {}
    assert actual_vault.md_links_index == {}
    assert actual_vault.tags_index == {}
    assert actual_vault.nonexistent_notes == []
    assert actual_vault.isolated_notes == []
    assert actual_vault.front_matter_index == {}


def test_vault_instantiation_needs_directory():
    with pytest.raises(TypeError):
        Vault()


def test_get_md_relpaths(mock_initial_vault):
    mock_output = mock_initial_vault._get_md_relpaths()
    assert isinstance(mock_output, list)


def test_get_md_relpaths_by_name(mock_initial_vault):
    mock_output = mock_initial_vault._get_md_relpaths_by_name()
    assert isinstance(mock_output, dict)


def test_get_wikilinks_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_wikilinks_index()
    assert isinstance(mock_output, dict)


def test_get_math_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_math_index()
    assert isinstance(mock_output, dict)


def test_get_embedded_files_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_embedded_files_index()
    assert isinstance(mock_output, dict)


def test_get_unique_wikilinks_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_unique_wikilinks_index()
    assert isinstance(mock_output, dict)


def test_get_tags_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_tags_index()
    assert isinstance(mock_output, dict)


def test_get_front_matter_index(mock_initial_vault):
    mock_output = mock_initial_vault._get_front_matter_index()
    assert isinstance(mock_output, dict)


def test_connect(mock_initial_vault):
    mock_output = mock_initial_vault.connect()

    assert mock_initial_vault.is_connected
    assert isinstance(mock_initial_vault.is_connected, bool)
    assert isinstance(mock_initial_vault.graph, nx.Graph)
    assert isinstance(mock_initial_vault.graph, nx.MultiDiGraph)
    assert isinstance(mock_initial_vault.backlinks_index, dict)
    assert isinstance(mock_initial_vault.wikilinks_index, dict)
    assert isinstance(mock_initial_vault.tags_index, dict)
    assert isinstance(mock_initial_vault.embedded_files_index, dict)
    assert isinstance(mock_initial_vault.math_index, dict)
    assert isinstance(mock_initial_vault.md_links_index, dict)
    assert isinstance(mock_initial_vault.nonexistent_notes, list)
    assert isinstance(mock_initial_vault.isolated_notes, list)
    assert isinstance(mock_initial_vault.front_matter_index, dict)

    # output is the vault object itself
    assert isinstance(mock_output, Vault)


def test_functions_to_fail_for_unconnected_vault(mock_initial_vault):
    # catch functions that require attributes set via connect method
    with pytest.raises(AttributeError):
        mock_initial_vault.get_backlinks('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_backlink_counts('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_wikilinks('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_tags('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_embedded_files('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_math_index('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_front_matter('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_md_links('A note that would not exist')
    with pytest.raises(AttributeError):
        mock_initial_vault.get_note_metadata()
