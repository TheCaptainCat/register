from register import create_app

if __name__ == '__main__':
    blnt = create_app()
    blnt.exec_cmd_args()
