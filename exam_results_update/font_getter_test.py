"""font_getter_test.py

该 module 是对 `font_getter.py` 的单元测试。
"""

import hashlib
import os
import unittest

import font_getter


class TestFontGetter(unittest.TestCase):
    """该类是 unittest 测试类。"""

    def setUp(self):
        """该方法用于初始化测试。它将清除测试将下载的文件。"""

        # 清理之前的测试结果
        if os.path.exists(font_getter.TARGET_FILE):
            os.remove(font_getter.TARGET_FILE)

    def test_download_and_extract_font(self):
        """主测试逻辑。"""

        # 调用 font_getter.py 中的下载和解压逻辑
        font_getter.main()

        # 检查文件是否存在
        self.assertTrue(os.path.exists(font_getter.TARGET_FILE), "文件未成功下载和解压！")

        # 计算文件的 SHA256 值
        with open(font_getter.TARGET_FILE, 'rb') as f:
            file_content = f.read()
            sha256_hash = hashlib.sha256(file_content).hexdigest()

        # 检查文件的 SHA256 值是否匹配
        expected_sha256 = '297b088424be212207df2ce8b98e335468b782aa6b96832af0b8b773d711e2b1'
        self.assertEqual(sha256_hash, expected_sha256, "文件的 SHA256 值不匹配！")

    def tearDown(self):
        """清理测试结果。"""

        if os.path.exists(font_getter.TARGET_FILE):
            os.remove(font_getter.TARGET_FILE)

if __name__ == '__main__':
    unittest.main()
