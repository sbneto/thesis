
retweets_names = [
	'8\\_Semesters',
	'\\_\\_ShesBrownSKIN',
	'\\_\\_tiki',
	'\\_CarGotThat',
	'AshKetchum151',
	'Becchappell',
	'bombaytricycle',
	'brandonlondon',
	'CalebGarling',
	'davidAmejia',
	'dsilverman',
	'ESPN\\_FirstTake',
	'Greektown1921',
	'HollywoodLadyj',
	'j4kebro',
	'jam\\_bu88',
	'justaholyfooool',
	'michael\\_palko',
	'mike\\_sprague',
	'mshowalter',
	'neiltyson',
	'oliviaaajayne\\_',
	'RealSkipBayliss',
	'Snoopy',
	'terrigolas',
]

replies_names = [
	'Ali\\_Diesel\\_',
	'EmmittWard',
	'essfardella',
	'esterrick',
	'HectorBesmonte',
	'hockeybychoice',
	'hollye83',
	'hottiemarkie33',
	'istoleursmartie',
	'JasonReedyOH420',
	'jccassiel',
	'kiafranklins\\_',
	'KurlyKonfektion',
	'Mahalia\\_Enares',
	'mark\\_purdie',
	'MeganDoesNOLA',
	'michel\\_andness',
	'Michel\\_andNess',
	'missRaichl',
	'MollytheGhost',
	'mton1996',
	'onlymystory',
	'PhantomRat',
	'phouse1964',
	'RazWorth',
	'Rhino108',
	'SarahMcCallumXX',
	'Serrae',
	'shanmilanowski',
	'shkeeber',
	'sjopierce',
	'SophieRaby',
	'StationBistro1',
	'VinnyG5',
]

non_tagged_names = [
	'24\\_Jag',
	'ahoynialler',
	'annesaurus',
	'AntDeRosa',
	'BadJerry20',
	'DaMontesMom\\_415',
	'esterrick',
	'ESTL63',
	'ethanklapper',
	'fatherdowling',
	'hypervocal',
	'majic1021',
	'MichaelAusiello',
	'Mrjscott',
	'Niallofficial',
	'NiallOfficial',
	'nickybyrneoffic',
	'nicoleoraha',
	'Reuters',
	'Serrae',
	'Supperphilly',
	'T\\_dot\\_Lee',
	'VictoriaLMathis',
	'WestlifeFansite',
	'whitehouse',
	'wulan\\_kyuufilan',
	'Zac\\_Hartlage14',
]

def replace_names(start_n, file, users):
	def user_count():
		nonlocal start_n
		start_n += 1
		return start_n
	users_map = {name: 'User\\_{}'.format(user_count()) for name in users}

	with open(file, 'r') as inf, open(file.replace('.tex', '_anon.tex'), 'w') as outf:
		data = inf.read()
		for name, anon in users_map.items():
			print('replacing {} for {}'.format(name, anon))
			data = data.replace(name, anon)
		outf.write(data)
	return start_n


i = 0
i = replace_names(i, 'tweets_table_retweets.tex', retweets_names)
i = replace_names(i, 'tweets_table_replies.tex', replies_names)
i = replace_names(i, 'tweets_table_nontagged.tex', non_tagged_names)
