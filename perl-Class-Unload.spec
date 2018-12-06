#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Unload
Version  : 0.11
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Class-Unload-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Class-Unload-0.11.tar.gz
Summary  : 'Unload a class'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Unload-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Test::Requires)

%description
This archive contains the distribution Class-Unload,
version 0.11:
Unload a class

%package dev
Summary: dev components for the perl-Class-Unload package.
Group: Development
Provides: perl-Class-Unload-devel = %{version}-%{release}

%description dev
dev components for the perl-Class-Unload package.


%package license
Summary: license components for the perl-Class-Unload package.
Group: Default

%description license
license components for the perl-Class-Unload package.


%prep
%setup -q -n Class-Unload-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Unload
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Unload/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Class/Unload.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Unload.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Unload/LICENSE
