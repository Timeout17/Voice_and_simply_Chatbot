from Project.src.data.DAO import MessageDAOClass

def test_empty_database(test_connection):

    dao = MessageDAOClass(test_connection)

    assert dao.get_message_count() == 0