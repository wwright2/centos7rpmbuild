%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}

Name:           perl-IO-Socket-Multicast
Version:        1.12
Release:        1%{?dist}
Summary:        Send and receive multicast messages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Socket-Multicast/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Interface) >= 0.94
Requires:       perl(IO::Interface) >= 0.94

%description
The IO::Socket::Multicast module subclasses IO::Socket::INET to enable you
to manipulate multicast groups. With this module (and an operating system
that supports multicasting), you will be able to receive incoming multicast
transmissions and generate your own outgoing multicast packets.

%prep
%setup -q -n IO-Socket-Multicast-%{version}

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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IO*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 1.12-1
- Specfile autogenerated by cpanspec 1.78.