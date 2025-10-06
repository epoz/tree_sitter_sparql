from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import platform

class Build(build_ext):
    def build_extensions(self):
        # Add compiler-specific flags
        if platform.system() == 'Windows':
            for ext in self.extensions:
                ext.extra_compile_args = ['/std:c11']
        else:
            for ext in self.extensions:
                ext.extra_compile_args = ['-std=c11']
        super().build_extensions()

# Read the tree-sitter parser
tree_sitter_sparql = Extension(
    'tree_sitter_sparql.binding',
    sources=[
        'bindings/python/binding.c',
        'src/parser.c',
    ],
    include_dirs=[
        'src',
    ],
    extra_compile_args=[
        '-std=c11',
    ] if platform.system() != 'Windows' else ['/std:c11'],
)

setup(
    packages=['tree_sitter_sparql'],
    package_dir={'tree_sitter_sparql': 'bindings/python/tree_sitter_sparql'},
    package_data={
        'tree_sitter_sparql': ['*.pyi', 'py.typed'],
    },
    ext_modules=[tree_sitter_sparql],
    cmdclass={'build_ext': Build},
)
