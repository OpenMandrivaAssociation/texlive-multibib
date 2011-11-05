# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/multibib
# catalog-date 2008-12-10 20:42:30 +0100
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-multibib
Version:	1.4
Release:	1
Summary:	Multiple bibliographies within one document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multibib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Multibib the creation of references to multiple bibliographies
within one document. It thus provides complementary
functionality to packages like bibunits and chapterbib, which
allow the creation of one bibliography for multiple, but
different parts of the document. Multibib is compatible with
inlinebib, natbib, and koma-script.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/multibib/mbplain.bst
%{_texmfdistdir}/bibtex/bst/multibib/mbunsrtdin.bst
%{_texmfdistdir}/makeindex/multibib/mbgglo.ist
%{_texmfdistdir}/makeindex/multibib/mbgind.ist
%{_texmfdistdir}/tex/latex/multibib/multibib.sty
%doc %{_texmfdistdir}/doc/latex/multibib/README
%doc %{_texmfdistdir}/doc/latex/multibib/bibtexall
%doc %{_texmfdistdir}/doc/latex/multibib/multibib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multibib/multibib.dtx
%doc %{_texmfdistdir}/source/latex/multibib/multibib.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
