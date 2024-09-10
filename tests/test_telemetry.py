from datachain.lib.dc import DataChain
from datachain.telemetry import is_enabled


def test_is_enabled():
    assert not is_enabled()


def test_telemetry_api_call(mocker, tmp_dir):
    patch_send = mocker.patch("iterative_telemetry.IterativeTelemetryLogger.send")

    DataChain.from_storage(tmp_dir.as_uri())
    assert patch_send.call_count == 1
    args = patch_send.call_args_list[0].args[0]
    extra = args.pop("extra")

    assert args == {"interface": "api", "action": "datachain_init", "error": None}

    assert "name" in extra
