import asyncio


async def asynchronous_task_sleep(seconds: int) -> None:
    """
    Asynchronous task that sleeps for the specified number of seconds.

    Args:
        seconds (int): Number of seconds to sleep.

    Returns:
        None
    """
    await asyncio.sleep(seconds)
    print(f"Asynchronous task sleep completed after {seconds} seconds")


async def asynchronous_task_network_request() -> None:
    """
    Asynchronous task that simulates making a network request.

    Returns:
        None
    """
    await asyncio.sleep(1)
    print("Asynchronous task making a network request")


async def asynchronous_task_file_io() -> None:
    """
    Asynchronous task that performs file I/O.

    Returns:
        None
    """
    await asyncio.to_thread(write_to_file)
    print("Asynchronous task writing to a file")


def write_to_file() -> None:
    """
    Synchronous function to write to a file.

    Note: This function is meant to be called within asyncio.to_thread.

    Returns:
        None
    """
    with open("example_file.txt", "w") as file:
        file.write("Asynchronous task writing to a file")


async def asynchronous_task_concurrent_execution() -> None:
    """
    Asynchronous task demonstrating concurrent execution using asyncio.gather.

    Returns:
        None
    """
    tasks = [asynchronous_task_sleep(2), asynchronous_task_network_request()]
    await asyncio.gather(*tasks)
    print("Asynchronous task running multiple tasks concurrently")


async def asynchronous_task_database_interaction() -> None:
    """
    Asynchronous task simulating interaction with a database.

    Returns:
        None
    """
    await asyncio.sleep(1)
    print("Asynchronous task interacting with a database")


async def asynchronous_task_external_api_call() -> None:
    """
    Asynchronous task simulating making an external API call.

    Returns:
        None
    """
    await asyncio.sleep(1)
    print("Asynchronous task making an external API call")


async def asynchronous_task_chaining_functions() -> None:
    """
    Asynchronous task chaining multiple functions.

    Returns:
        None
    """
    await asynchronous_task_sleep(1)
    await asynchronous_task_network_request()
    print("Asynchronous task chaining functions")


async def asynchronous_task_using_asyncio_wait() -> None:
    """
    Asynchronous task using asyncio.wait for concurrent execution.

    Returns:
        None
    """
    tasks = [asynchronous_task_sleep(1), asynchronous_task_network_request()]
    task_instances = [asyncio.create_task(task) for task in tasks]
    done, pending = await asyncio.wait(task_instances)
    print("Asynchronous task using asyncio.wait")


async def asynchronous_task_with_error_handling() -> None:
    """
    Asynchronous task demonstrating error handling.

    Returns:
        None
    """
    try:
        await asyncio.sleep(1)
        raise Exception("Simulated error")
    except Exception as e:
        print(f"Asynchronous task caught an exception - {e}")


async def asynchronous_task_with_cancellation() -> None:
    """
    Asynchronous task demonstrating cancellation.

    Returns:
        None
    """
    try:
        await asyncio.sleep(5)
        print("Asynchronous task: This should not be printed")
    except asyncio.CancelledError:
        print("Asynchronous task: Task was cancelled")


async def asynchronous_task_with_timeout() -> None:
    """
    Asynchronous task demonstrating timeout.

    Returns:
        None
    """
    try:
        await asyncio.wait_for(asynchronous_task_sleep(1), timeout=3)
        print("Asynchronous task completed within the timeout")
    except asyncio.TimeoutError:
        print("Asynchronous task: Timeout exceeded")


async def asynchronous_task_with_conditional_execution(condition: bool) -> None:
    """
    Asynchronous task demonstrating conditional execution.

    Args:
        condition (bool): Boolean condition for execution.

    Returns:
        None
    """
    if condition:
        await asynchronous_task_sleep(1)
        print("Asynchronous task: Condition is True")
    else:
        print("Asynchronous task: Condition is False")


# Example of running these functions
async def main() -> None:
    await asynchronous_task_sleep(1)
    await asynchronous_task_network_request()
    await asynchronous_task_file_io()
    await asynchronous_task_concurrent_execution()
    await asynchronous_task_database_interaction()
    await asynchronous_task_external_api_call()
    await asynchronous_task_chaining_functions()
    await asynchronous_task_using_asyncio_wait()
    await asynchronous_task_with_error_handling()
    await asynchronous_task_with_cancellation()
    await asynchronous_task_with_timeout()
    await asynchronous_task_with_conditional_execution(True)


# Example of running these functions
if __name__ == "__main__":
    asyncio.run(main())
