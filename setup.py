import os
import logging

import setuptools

# Shady... But I can't import setuptools._distutils without breaking stuff...
import distutils.command.build_scripts


class build_scripts(distutils.command.build_scripts.build_scripts):
    def finalize_options(self):
        super().finalize_options()
        self.build_dir = os.path.join(self.build_dir, "rez")

    def run(self) -> None:
        logging.getLogger().info("running rez's customized build_scripts command")
        return super().run()


setuptools.setup(
    name="rez-wheel-prod-experiment",
    version="1.0.0",
    packages=["src/rez"],
    scripts=["scripts/test.py"],
    cmdclass={"build_scripts": build_scripts},
)
