{pkgs, ...}:
with pkgs;
  python3Packages.buildPythonPackage {
    name = "ical2json";
    format = "pyproject";
    src = ./.;
    propagatedBuildInputs = with python3Packages; [
      hatchling
      icalendar
      requests
    ];
  }
