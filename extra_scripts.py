import os

Import("env")

env.BuildSources(
    os.path.join("$PROJECT_DIR", "micro_ros_stm32cubemx_utils", "extra_sources"),
    os.path.join("$PROJECT_DIR", "micro_ros_stm32cubemx_utils", "extra_sources", "microros_transports"),
    os.path.join("$PROJECT_DIR", "micro_ros_stm32cubemx_utils", "microros_static_library", "libmicroros"),
    # os.path.join("$PROJECT_DIR", "micro_ros_stm32cubemx_utils", "microros_static_library", "libmicroros", "microros_include")

)