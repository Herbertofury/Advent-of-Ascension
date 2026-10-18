"""Generated archive faults; these tests never certify Minecraft/Hari execution."""
import io
import unittest
import warnings
import zipfile
from inspect_hari_contract import archive_inventory


def archive(rows):
    stream=io.BytesIO()
    with warnings.catch_warnings(),zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as output:
        warnings.simplefilter('ignore',UserWarning)
        for name,body in rows:output.writestr(name,body)
    return stream.getvalue()


class CompleteArchiveInspection(unittest.TestCase):
    # Generated minimal header for inventory only; Java independently parses real constant pools.
    header=b'\xca\xfe\xba\xbe\x00\x00\x00\x3d\x00\x01'
    def test_every_nested_member_is_counted(self):
        nested=archive([('generated/B.class',self.header),('data.txt',b'complete')])
        self.assertEqual(archive_inventory(archive([('generated/A.class',self.header),('nested.jar',nested)]),'generated'),(2,2))
    def test_duplicate_member_rejected(self):
        with self.assertRaises(ValueError):archive_inventory(archive([('A.class',self.header),('A.class',self.header)]),'generated')
    def test_invalid_class_rejected(self):
        with self.assertRaises(ValueError):archive_inventory(archive([('A.class',b'not a class')]),'generated')
    def test_truncated_archive_rejected(self):
        with self.assertRaises(zipfile.BadZipFile):archive_inventory(archive([('A.class',self.header)])[:-24],'generated')
    def test_unreadable_nested_archive_rejected(self):
        with self.assertRaises(zipfile.BadZipFile):archive_inventory(archive([('A.class',self.header),('broken.jar',b'not a zip')]),'generated')
    def test_multi_release_members_are_retained(self):
        self.assertEqual(archive_inventory(archive([('A.class',self.header),('META-INF/versions/17/A.class',self.header)]),'generated'),(2,1))


if __name__=='__main__':unittest.main()
