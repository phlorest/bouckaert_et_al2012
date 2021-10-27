from setuptools import setup


setup(
    name='cldfbench_bouckaert_et_al2012',
    py_modules=['cldfbench_bouckaert_et_al2012'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bouckaert_et_al2012=cldfbench_bouckaert_et_al2012:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
