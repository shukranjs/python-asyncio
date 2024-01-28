import asyncio
import pytest
from async_functions import (
    asynchronous_task_sleep,
    asynchronous_task_network_request,
    asynchronous_task_file_io,
    asynchronous_task_concurrent_execution,
    asynchronous_task_database_interaction,
    asynchronous_task_external_api_call,
    asynchronous_task_chaining_functions,
    asynchronous_task_using_asyncio_wait,
    asynchronous_task_with_error_handling,
    asynchronous_task_with_cancellation,
    asynchronous_task_with_timeout,
    asynchronous_task_with_conditional_execution,
)


@pytest.mark.asyncio
async def test_asynchronous_task_sleep():
    await asynchronous_task_sleep(1)


@pytest.mark.asyncio
async def test_asynchronous_task_network_request():
    await asynchronous_task_network_request()


@pytest.mark.asyncio
async def test_asynchronous_task_file_io():
    await asynchronous_task_file_io()


@pytest.mark.asyncio
async def test_asynchronous_task_concurrent_execution():
    await asynchronous_task_concurrent_execution()


@pytest.mark.asyncio
async def test_asynchronous_task_database_interaction():
    await asynchronous_task_database_interaction()


@pytest.mark.asyncio
async def test_asynchronous_task_external_api_call():
    await asynchronous_task_external_api_call()


@pytest.mark.asyncio
async def test_asynchronous_task_chaining_functions():
    await asynchronous_task_chaining_functions()


@pytest.mark.asyncio
async def test_asynchronous_task_using_asyncio_wait():
    await asynchronous_task_using_asyncio_wait()


@pytest.mark.asyncio
async def test_asynchronous_task_with_error_handling():
    await asynchronous_task_with_error_handling()


@pytest.mark.asyncio
async def test_asynchronous_task_with_cancellation():
    task = asyncio.create_task(asynchronous_task_with_cancellation())
    await asyncio.sleep(2)  # Allow some time for the task to start
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


@pytest.mark.asyncio
async def test_asynchronous_task_with_timeout():
    await asynchronous_task_with_timeout()


@pytest.mark.asyncio
async def test_asynchronous_task_with_conditional_execution():
    await asynchronous_task_with_conditional_execution(True)
    await asynchronous_task_with_conditional_execution(False)
