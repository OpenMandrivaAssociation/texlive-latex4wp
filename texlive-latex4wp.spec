%global tl_name latex4wp
%global tl_revision 68096

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A LaTeX guide specifically designed for word processor users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex4wp
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"LaTeX for Word Processor Users" is a guide that helps converting
knowledge and techniques of word processing into the LaTeX typesetting
environment. It aims at helping WP users use LaTeX instead.

