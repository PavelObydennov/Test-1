import pytest



@pytest.mark.db
def test_users_exist(db_cur):
    db_cur.execute("SELECT COUNT(*) FROM users")
    count = db_cur.fetchone()[0]
    print("Users in table:", count)
    assert count > 0

