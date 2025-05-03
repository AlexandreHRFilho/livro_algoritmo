grid	=	[['.',	'.',	'.',	'.',	'.',	'.'],
								['.',	'O',	'O',	'.',	'.',	'.'],
								['O',	'O',	'O',	'O',	'.',	'.'],
								['O',	'O',	'O',	'O',	'O',	'.'],
								['.',	'O',	'O',	'O',	'O',	'O'],
								['O',	'O',	'O',	'O',	'O',	'.'],
								['O',	'O',	'O',	'O',	'.',	'.'],
								['.',	'O',	'O',	'.',	'.',	'.'],
								['.',	'.',	'.',	'.',	'.',	'.']]

for x in range(6):  # 9 linhas
    for y in range(9):  # 6 colunas
        print(grid[y][x], end=' ')

    print()  # Nova linha após cada linha do grid

