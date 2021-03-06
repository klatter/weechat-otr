# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-public-methods

from __future__ import unicode_literals

import sys

from weechat_otr_test.weechat_otr_test_case import WeechatOtrTestCase

import weechat_otr

class HtmlEscapePolicyTestCase(WeechatOtrTestCase):

    def test_default_html_escape_policy(self):
        result = weechat_otr.message_out_cb(None, None, 'server',
            ':nick!user@host PRIVMSG friend :< > " \' &')
        self.assertEqual(result, 'PRIVMSG friend :< > " \' &')

    def test_html_escape_policy(self):
        sys.modules['weechat'].config_options[
            'otr.policy.server.nick.friend.html_escape'] = 'on'

        result = weechat_otr.message_out_cb(None, None, 'server',
            ':nick!user@host PRIVMSG friend :< > " \' &')
        self.assertEqual(result, 'PRIVMSG friend :&lt; &gt; " \' &amp;')

    def test_html_escape_policy_non_ascii(self):
        sys.modules['weechat'].config_options[
            'otr.policy.server.nick.gefährte.html_escape'] = 'on'

        result = weechat_otr.message_out_cb(None, None, 'server',
            ':nick!user@host PRIVMSG gefährte :< > " \' &')
        self.assertEqual(result, weechat_otr.PYVER.to_str(
            'PRIVMSG gefährte :&lt; &gt; " \' &amp;'))
