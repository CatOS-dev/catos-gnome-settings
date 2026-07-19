from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ALL_INI = ROOT / "etc/skel/.config/dconf/all.ini"
USER_DB = ROOT / "etc/skel/.config/dconf/user"


class DconfDefaultsTests(unittest.TestCase):
    def dump_user_database(self) -> str:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir) / ".config"
            dconf_dir = config_dir / "dconf"
            dconf_dir.mkdir(parents=True)
            shutil.copy2(USER_DB, dconf_dir / "user")
            env = os.environ.copy()
            env.update({"HOME": tmpdir, "XDG_CONFIG_HOME": str(config_dir)})
            return subprocess.run(
                ["dconf", "dump", "/"],
                check=True,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
            ).stdout

    def test_text_export_matches_binary_database(self):
        self.assertEqual(ALL_INI.read_text(encoding="utf-8"), self.dump_user_database())

    def test_ptyxis_is_the_configured_terminal(self):
        dump = self.dump_user_database()
        self.assertIn("selected-terminal='Ptyxis'", dump)
        self.assertIn("[org/gnome/Ptyxis]", dump)
        self.assertIn("font-name='JetBrainsMono Nerd Font Mono 10'", dump)
        self.assertIn("use-system-font=false", dump)
        self.assertIn("org.gnome.Ptyxis.desktop", dump)
        self.assertNotIn("org.gnome.Console", dump)
        self.assertNotIn("[org/gnome/Console]", dump)


if __name__ == "__main__":
    unittest.main()
