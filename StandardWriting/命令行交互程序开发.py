
# 用Python如何正确开发命令行交互程序

import cmd


class Query(cmd.Cmd):
    intro = "用户信息查询系统，输入help或者？查看帮助。\n"
    prompt = 'query>'

    def do_query_by_id(self, arg):
        '根据用户id查询用户'
        self.query_by_id(arg)

    def do_query_by_name(self, arg):
        '根据用户名查询'
        self.query_by_name(arg)

    def do_exit(self, _):
        '退出'
        exit(0)

    def query_by_id(self, user_id):
        print(f'查询id为：{user_id}对应的用户')

    def query_by_name(self, user_name):
        print(f'查询用户名为：{user_name}的用户')


if __name__ == '__main__':
    Query().cmdloop()
