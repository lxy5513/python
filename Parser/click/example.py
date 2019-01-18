import click
@click.command()
@click.option('--rate', type=float, help='rate')   # 指定 rate 是 float 类型
def show(rate):
    click.echo('rate: %s' % rate)
if __name__ == '__main__':
    show()
