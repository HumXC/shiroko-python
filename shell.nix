with import <nixpkgs> { };
pkgs.mkShell {
  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc
      ]}:$LD_LIBRARY_PATH
  '';
}
