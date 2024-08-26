from Pages import SearchHelper


def test_search(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.enter_word("Hello")
    main_page.click_on_the_search_button()
    elements = main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements
