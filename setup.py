from setuptools import setup

def readme():
	with open('README.md') as f:
		return f.read()
setup(name='trabajo-py',
	version='0.0.1',
	description='Esta es la primera descripcion',
	lang_description='Esta es la segunda descripcion',
	classifiers=[
		'Development Status :: 1 - Alpha',
		'Programming Language :: Python :: 3.5',
		'Topic :: Software :: Learning'
	],
	keywords='prueba aprendiendo',
	url='https://github.com/hpuerta/trabajo-py',
	author='Harry Puerta',
	author_mail='hpuertam@unal.edu.co',
	license="MIT"
	)