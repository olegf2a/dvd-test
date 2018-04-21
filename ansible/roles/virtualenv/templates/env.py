#!/usr/bin/env python

import argparse, re, os, sys, collections, yaml

ENV_FILE = os.environ.get('ENV_FILE')

try:
	from shlex import quote as shell_quote
except ImportError:
	def shell_quote(s):
		return s.replace('"', '"\\""')

def value_str(s):
	if isinstance(s, bool):
		return 'true' if s else 'false'
	if isinstance(s, int):
		return str(s)
	if not s:
		return s
	return shell_quote(str(s))

def get_env_vars():
	with open(ENV_FILE, 'r') as stream:
		env_vars = yaml.load(stream)
	d = collections.OrderedDict(sorted(env_vars.items()))
	return { k: d[k] for k in d }

def set_env_var(env_vars, var, val):
	if val.lower() == 'true':
		env_vars[var] = True
	elif val.lower() == 'false':
		env_vars[var] = False
	else:
		env_vars[var] = val
	return env_vars

def update_env_vars(env_vars):
	with open(ENV_FILE, 'w') as stream:
		yaml.dump(env_vars, stream, default_flow_style=False)

def dump_env_vars(env_vars, fmt, stream):
	if fmt == 'yaml':
		yaml.dump(env_vars, stream, default_flow_style=False)
	elif fmt == 'keys':
		for k in env_vars:
			stream.write("%s\n" % k)
	elif fmt == 'bash':
		for k in env_vars:
			stream.write("export %s=\"%s\"\n" % (k, value_str(env_vars[k])))

def save_env_vars(env_vars, fmt, filename):
	with open(filename, 'r+') as fp:
		fp.truncate()
		fp.seek(0)
		dump_env_vars(env_vars, fmt, fp)

class EnvironmentCompleter:
	def __init__(self, env_vars):
		self.env_keys = env_vars.keys()

	def __call__(self, prefix, **kwargs):
		return (k for k in self.env_keys if k.startswith(prefix))


if __name__ == '__main__':
	env_vars = get_env_vars()

	parser = argparse.ArgumentParser()
	parser.add_argument('--set', '-s', nargs=2, help='set variable', metavar=('variable', 'value')).completer = EnvironmentCompleter(env_vars)
	parser.add_argument('--get', '-g', nargs=1, help='get variables', metavar=('variable',)).completer = EnvironmentCompleter(env_vars)
	parser.add_argument('--delete', '-d', nargs='?', help='delete variable', metavar=('variable',)).completer = EnvironmentCompleter(env_vars)
	parser.add_argument('--list', '-l', choices=[ 'yaml', 'bash', 'nginx', 'keys' ], help='yaml | bash | nginx | keys', metavar=('format',))
	parser.add_argument('--outfile', '-o', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

	try:
		import argcomplete
		argcomplete.autocomplete(parser)
	except ImportError:
		pass

	args = parser.parse_args()

	if args.set and (re.match(r"([A-Z0-9_]{1,4096})", args.set[0]) or args.set[0] == ''):
		update_env_vars(set_env_var(env_vars, args.set[0], args.set[1]))

	elif args.delete:
		if args.delete in env_vars:
			del env_vars[args.delete]
			update_env_vars(env_vars)

	elif args.list:
		dump_env_vars(env_vars, args.list, args.outfile)

	else:
		if args.get:
			for k in env_vars:
				if re.match(args.get[0], k):
					args.outfile.write("%s: %s\n" % (k, env_vars[k]))
		else:
			dump_env_vars(env_vars, 'yaml', args.outfile)

	sys.exit()
