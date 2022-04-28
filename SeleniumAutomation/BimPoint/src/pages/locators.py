from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    SEARCH_TEXT = (By.NAME, 'q')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass


class AppLoginPageLocators(object):
    """A class for app login page locators. Second part of login page locators appears after clicking Continue button
    https://uat1-app.bim-point.com"""
    # Username textfield <input type="email" class="form-control" id="login-username" placeholder="Username" name="email">
    USERNAME_TEXT = (By.ID, "login-username")
    # Continue button <button type="submit" class="btn btn-info btn-flat pull-right bp-login-btn" id="btn-login">Continue</button>
    CONTINUE_BUTTON = (By.ID, "btn-login")
    # These buttons are available after providing username and clicking Continue button
    # Pasword textfield <input type="password" class="form-control" id="login-password" placeholder="Password" name="password">
    PASSWORD_TEXT = (By.ID, "login-password")
    # Login button <button type="submit" class="btn btn-info btn-flat pull-right bp-login-btn" id="btn-login">Login</button>
    LOGIN_BUTTON = (By.ID, "btn-login")

