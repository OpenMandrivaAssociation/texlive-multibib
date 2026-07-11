%global tl_name multibib
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Multiple bibliographies within one document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multibib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package the creation of references to multiple bibliographies within
one document. It thus provides complementary functionality to packages
like bibunits and chapterbib, which allow the creation of one
bibliography for multiple, but different parts of the document. Multibib
is compatible with inlinebib, natbib, and koma-script.

