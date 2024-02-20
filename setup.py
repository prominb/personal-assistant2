from setuptools import setup, find_namespace_packages

setup(
    name='personal-assistant',
    version='0.0.1',
    description='Personal assistant helps you organize your notes and address book.',
    url='https://github.com/prominb/personal-assistant',
    author='Olds coders',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    include_package_data=True,
    entry_points={'console_scripts': ['run-assistant = personal_assistant:run_bot']},
    zip_safe=False
)
