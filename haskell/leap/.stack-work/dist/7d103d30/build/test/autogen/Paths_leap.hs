{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_leap (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [1,5,1,9] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\bin"
libdir     = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\lib\\x86_64-windows-ghc-8.4.3\\leap-1.5.1.9-2RWU45upSth5hKgQEinqez-test"
dynlibdir  = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\lib\\x86_64-windows-ghc-8.4.3"
datadir    = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\share\\x86_64-windows-ghc-8.4.3\\leap-1.5.1.9"
libexecdir = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\libexec\\x86_64-windows-ghc-8.4.3\\leap-1.5.1.9"
sysconfdir = "C:\\Users\\Asus\\Exercism\\haskell\\leap\\.stack-work\\install\\dbe016db\\etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "leap_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "leap_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "leap_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "leap_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "leap_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "leap_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "\\" ++ name)
