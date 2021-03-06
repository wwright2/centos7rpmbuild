%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}

Name:           perl-Crypt-Blowfish
Version:        2.14
Release:        1%{?dist}
Summary:        Perl Blowfish encryption module
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-Blowfish/
Source0:        http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-Blowfish-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Blowfish is capable of strong encryption and can use key sizes up to 56
bytes (a 448 bit key). You're encouraged to take advantage of the full key
size to ensure the strongest encryption possible from this module.

%prep
%setup -q -n Crypt-Blowfish-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes COPYRIGHT README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 2.14-1
- Specfile autogenerated by cpanspec 1.78.
