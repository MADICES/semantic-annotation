{ pkgs ? (import <nixpkgs> {}) }:
pkgs.mkShell {
  packages = [
    pkgs.unzip
    pkgs.jq
    pkgs.python311
  ];
  shellHook = ''
    source venv/bin/activate
  '';
}
