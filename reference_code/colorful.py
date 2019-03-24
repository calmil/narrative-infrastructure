import colorful.colors

# create a colored string using clever method translation
print(colorful.bold_white('Hello World'))
# create a colored string using `str.format()`
print('{c.bold}{c.lightCoral_on_white}Hello World{c.reset}'.format(c=colorful))

# nest colors
print(colorful.red('red {0} red'.format(colorful.white('white'))))
print(colorful.red('red' + colorful.white(' white ', nested=True) + 'red'))

# combine styles with strings
print(colorful.bold & colorful.red | 'Hello World')

# use true colors
colorful.use_true_colors()

# extend default color palette
colorful.update_palette({'mint': '#c5e8c8'})
print(colorful.mint_on_snow('Wow, this is actually mint'))

# choose a predefined style
colorful.use_style('solarized')
# print the official solarized colors
print(colorful.yellow('yellow'), colorful.orange('orange'),
    colorful.red('red'), colorful.magenta('magenta'),
    colorful.violet('violet'), colorful.blue('blue'),
    colorful.cyan('cyan'), colorful.green('green'))

# directly print with colors
colorful.print('{c.bold_blue}Hello World{c.reset}')

# choose specific color mode for one block
with colorful.with_8_ansi_colors() as c:
    print(c.bold_green('colorful is awesome!'))

# create and choose your own color palette
MY_COMPANY_PALETTE = {
    'companyOrange': '#f4b942',
    'companyBaige': '#e8dcc5'
}
with colorful.with_palette(my_company_palette) as c:
    print(c.companyOrange_on_companyBaige('Thanks for choosing our product!'))

# use f-string (only Python >= 3.6)
print(f'{colorful.bold}Hello World')

# support for chinese
print(colorful.red('你好'))